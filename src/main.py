


from textnode import TextNode, TextType


def main():

    text_node = TextNode("This is some text", TextType.LINKS_TEXT, "https://www.boot.dev")
    print(text_node)


if __name__ == "__main__":
    main()