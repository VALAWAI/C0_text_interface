from threading import Thread

from valawai_sr import Channel, TextMessage, env

env.add("speaker", "HUMAN")
"""The identifier for the participant in the dialogue."""


def consumer():
    def new_message(ch, method, properties, body):
        message: TextMessage = TextMessage.from_json(body)
        if message.speaker != env.speaker:
            print(f"{message.speaker}: {message.text}")

    channel = Channel()
    channel.configure_consume(env.text_interface_key, new_message)
    channel.start_consuming()


def publisher():
    channel = Channel()
    while True:
        input_text = input("> ")
        message = TextMessage(speaker=env.speaker, text=input_text)
        channel.publish(env.text_interface_key, message)


def main():
    Thread(target=consumer).start()
    publisher()


if __name__ == "__main__":
    main()
