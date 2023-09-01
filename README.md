# VALAWAI SR C0 Text Interface

## Description

This C0 component implements a simple text interface for the Social Robots VALAWAI applications.

Text interfaces constitute the simplest form of human-computer interaction, allowing users to use typed commands or textual inputs, which is a direct and efficient means of communication with a system.
Despite the advent of graphical user interfaces (GUIs) which offer more visually intuitive interactions, text interfaces remain relevant due to their lightweight nature and simplicity.
Consequently, the reduced complexity allows to focus on other aspects of the system, which is useful during the debugging phase of a project.

With this component it is possible to input dialogue in the Social Robots VALAWAI system, and receive the corresponding responses.
The component can be customised with the identifier for the participant in the dialogue.
The input is performed with a simple text interface, and the output is displayed in the same interface.

The component runs in a _Docker_ container, and communicates with a _RabbitMQ_ message broker.

## Data Flow

This component uses a single channel (or _topic_ or _routing key_), `valawai.c0.text-interface`, to communicate with the message broker using the `amq.topic` exchange, which broadcasts the messages to all the listeners bound to it with the same routing key.

This channel is intended for dialogue messages containing text.
Subscribing to this channel allows to receive the dialogue messages, and publishing to this channel allows to send them.

The messages exchanged are _JSON_ objects with the following structure:

```json
{
  "version": "0.0.1", // The version of the format.
  "speaker": "HUMAN", // Identifier of the author of the message.
  "text": "Hello, World!", // The text of the message.
  "timestamp": "2019-08-24T14:15:22Z" // The timestamp of the message.
}
```

## Control Flow

This component does not use any control flow channel.

## Usage

Writing text in the terminal allows to input messages, and the responses from the broker are displayed in the same terminal.

The component is configurable with the following environment variables, with the default value indicated in parentheses:

- RMQ_HOST (`host.docker.internal`) The hostname of the message broker.
- TEXT_INTERFACE_KEY (`valawai.c0.text-interface`) The channel to use for dialogue messages.
- EXCHANGE (`amq.topic`) The exchange to use for dialogue messages.
- SPEAKER (_HUMAN_) The identifier for the participant in the dialogue.
