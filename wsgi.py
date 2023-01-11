from app import create_app

app = create_app()

if __name__ == "__main__":
    # Servidor de desenvolvimento apenas. NÃO USAR EM PRODUÇÃO
    app.run("127.0.0.1", 8080, True)
