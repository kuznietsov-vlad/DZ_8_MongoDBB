from models import Author, Quote

while True:
    command = input(">>> ")

    if command == "exit":
        break

    try:
        cmd, value = command.split(":", 1)
        value = value.strip()

        if cmd == "name":
            author = Author.objects(fullname=value).first()
            if author:
                for q in Quote.objects(author=author):
                    print(q.quote)

        elif cmd == "tag":
            for q in Quote.objects(tags=value):
                print(q.quote)

        elif cmd == "tags":
            tags = value.split(",")
            for q in Quote.objects(tags__in=tags):
                print(q.quote)

    except:
        print("Невірна команда")