"""Module defining encoders."""
from src.encoders.encoder import EncoderBase
from src.encoders.transformer import TransformerEncoder
from src.encoders.rnn_encoder import RNNEncoder
from src.encoders.cnn_encoder import CNNEncoder
from src.encoders.mean_encoder import MeanEncoder
from src.encoders.audio_encoder import AudioEncoder
from src.encoders.image_encoder import ImageEncoder


str2enc = {"rnn": RNNEncoder, "brnn": RNNEncoder, "cnn": CNNEncoder,
           "transformer": TransformerEncoder, "img": ImageEncoder,
           "audio": AudioEncoder, "mean": MeanEncoder}

__all__ = ["EncoderBase", "TransformerEncoder", "RNNEncoder", "CNNEncoder",
           "MeanEncoder", "str2enc"]
