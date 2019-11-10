"""Module defining decoders."""
from src.decoders.decoder import DecoderBase, InputFeedRNNDecoder, \
    StdRNNDecoder
from src.decoders.transformer import TransformerDecoder
from src.decoders.cnn_decoder import CNNDecoder


str2dec = {"rnn": StdRNNDecoder, "ifrnn": InputFeedRNNDecoder,
           "cnn": CNNDecoder, "transformer": TransformerDecoder}

__all__ = ["DecoderBase", "TransformerDecoder", "StdRNNDecoder", "CNNDecoder",
           "InputFeedRNNDecoder", "str2dec"]
