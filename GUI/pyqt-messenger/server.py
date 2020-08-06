import time
from datetime import datetime

from flask import Flask, request, Response

app = Flask(__name__)

messages = [
    {'name': 'Mary', 'time': time.time(), 'text': 'Привет'},
    {'name': 'Nick', 'time': time.time(), 'text': 'Привет'},
]

# Tag templates.
p_wrap = '<p>{}</p>'
br_wrap = '{}<br>'


def make_message(**kwargs):
    message = {'time': time.time()}
    message.update(kwargs)
    return message


@app.route("/send", methods=['POST'])
def send():

    name = request.json.get('name')
    text = request.json.get('text')
    if not (name and isinstance(name, str) and
            text and isinstance(text, str)):
        return Response(status=400)

    messages.append(make_message(name=name, text=text))

    botanswer = {'name': 'SkillBot'}
    if text == '/whoami':
        botanswer.update({'text': 'Your name is ' + name})
        messages.append(make_message(**botanswer))

    elif text == '/repeat':
        # NOTE: Just a copy of previous message. With same vals.
        previous_message = dict(messages[-2])
        previous_message['time'] = time.time()
        messages.append(previous_message)

    elif text.startswith('@'):
        # EXAMPLE: @eliz How are you?
        sentence = text.split(' ')
        address = sentence[0][1:]
        text = ' '.join(sentence[1:])
        target = {'name': address}
        for x in messages[::-1]:
            if x['name'] == address:
                target.update(x)
                break

        botanswer.update({
            'text': f'{name} in response to {target}\n{text}'
        })
        messages.append(make_message(**botanswer))

    return Response(status=200)


def filter_by_key(elements, key, threshold):
    filtered_elements = []

    for element in elements:
        if element[key] > threshold:
            filtered_elements.append(element)

    return filtered_elements


@app.route("/messages")
def messages_view():
    after = request.args.get('after')
    if not after:
        # Show last 100 messages.
        withbreaks = [br_wrap.format(x) for x in messages[-100:]]
        res = ''.join(withbreaks)
        return res

    try:
        after = float(after)
    except ValueError:
        return Response(status=400)

    filtered = filter_by_key(messages, key='time', threshold=after)
    return {'messages': filtered}


@app.route("/")
def hello():
    return "Hello, World! <a href='/status'>Статус</a>"


@app.route("/status")
def status():
    usernames = set()
    for x in messages:
        usernames.add(x['name'])

    res = {
        'status': '200 OK',
        'name': 'Skillbox Messenger',
        'time': datetime.now(),
        'total users': len(usernames),
        'total messages': len(messages),
    }
    # Format each item to `k: v` view.
    formatted = ['{:20}: {}'.format(k, v) for k, v in res.items()]
    # Add breaks to the end of sentence.
    withbreaks = [br_wrap.format(x) for x in formatted]
    return ''.join(withbreaks)


if __name__ == "__main__":
    app.run()
