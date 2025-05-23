import http.server
import ssl
from functools import partial
from server_logger import Logger
import socket

# 定义服务器地址和端口
server_ip = '::'
server_port = 26661
server_address = (server_ip, server_port)
target_directory = "F:/FileCDN"

# 创建SSL上下文
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./keys/cert.pem', keyfile='./keys/key.pem')

# 创建自定义Handler
handler = partial(http.server.SimpleHTTPRequestHandler, directory=target_directory)

# 实例化日志对象
logger = Logger()


# 自定义支持IPv6的服务器类
class DualStackHTTPServer(http.server.HTTPServer):
    address_family = socket.AF_INET6


# 创建HTTPServer实例
httpd = DualStackHTTPServer(server_address, handler)

# 包装SSL套接字
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

logger.log(f"HTTPS服务器已启动，访问：https://{server_ip}:{server_port}")

try:
    # 启动服务器
    httpd.serve_forever()
except KeyboardInterrupt:
    logger.log("\n收到中断信号，正在关闭服务器...")
    httpd.shutdown()  # 停止服务器循环
    httpd.server_close()  # 关闭底层socket
    logger.log("HTTP服务器已停止。")
