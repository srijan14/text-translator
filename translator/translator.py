import sys,os
import onmt.opts as opts
from onmt.translate.translator import build_translator
from onmt.utils.parse import ArgumentParser


class Translator:
    def __init__(self):
        self.model=None
        return

    def load_model(self,path=None):

        if path is None or not os.path.exists(os.path.abspath(
                os.path.join(os.getcwd(), path))):
            print("No model present at the specified path : {}".format(path))

        parser = ArgumentParser(description='translate.py')
        opts.config_opts(parser)

        opts.translate_opts(parser)
        opt = parser.parse_args(["--model", path])
        self.model = build_translator(opt, report_score=True)
        return

    def translate(self,inp=None):

        if inp is None:
            print("None type value provided as input")
            raise Exception("Provide valid input value")

        if self.model is None:
            print("Please do a load_model with the model path first, before running the translate")

        response = self.model.translate(src=[inp],batch_size=1)
        print("Translated Text is")
        for val in response:
            print("{}".format(val))


if __name__=="__main__":
    temp = Translator()
    temp.load_model(path="./model/model.pt")
    temp.translate("What is your name?")
