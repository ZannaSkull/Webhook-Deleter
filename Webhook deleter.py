import requests

def Delete(webhook_url: str) -> None:
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhook deletato")
    else:
        print(f"Impossibile cancellare il webhook. Num Errore: {response.status_code}")

if __name__ == "__main__":
    wrbhook = input("Inserisci l'URL del webhook di Discord da cancellare: ")
    Delete(wrbhook)
