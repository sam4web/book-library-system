from db.database import Library


def main():
    library = Library()
    library.create_tables()


if __name__ == "__main__":
    main()
