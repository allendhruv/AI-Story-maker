from image_analysis import *
from pk_openai import*
from sns import *
def main():
    # img_path=input("Enter Image")
    # img_analysis_initialize(img_path)
    # show_details()
    sns_initialize()
    openai_initialize()

if __name__ == "__main__":
    main()
