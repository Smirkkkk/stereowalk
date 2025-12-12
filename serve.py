#!/usr/bin/env python3
"""
Live Server with auto-reload for development
"""

from livereload import Server

def main():
    server = Server()
    
    # 监控所有 HTML, CSS, JS 文件的变化
    server.watch('*.html')
    server.watch('static/css/*.css')
    server.watch('static/js/*.js')
    server.watch('static/images/*')
    
    # 启动服务器
    print("🚀 Live Server 启动中...")
    print("📝 访问: http://localhost:8080")
    print("✨ 文件改动后会自动刷新浏览器")
    print("⌨️  按 Ctrl+C 停止服务器")
    
    server.serve(port=8080, host='localhost', root='.')

if __name__ == '__main__':
    main()


