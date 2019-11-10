"""  Attention and normalization modules  """
from src.modules.util_class import Elementwise
from src.modules.gate import context_gate_factory, ContextGate
from src.modules.global_attention import GlobalAttention
from src.modules.conv_multi_step_attention import ConvMultiStepAttention
from src.modules.copy_generator import CopyGenerator, CopyGeneratorLoss, \
    CopyGeneratorLossCompute
from src.modules.multi_headed_attn import MultiHeadedAttention
from src.modules.embeddings import Embeddings, PositionalEncoding, \
    VecEmbedding
from src.modules.weight_norm import WeightNormConv2d
from src.modules.average_attn import AverageAttention

__all__ = ["Elementwise", "context_gate_factory", "ContextGate",
           "GlobalAttention", "ConvMultiStepAttention", "CopyGenerator",
           "CopyGeneratorLoss", "CopyGeneratorLossCompute",
           "MultiHeadedAttention", "Embeddings", "PositionalEncoding",
           "WeightNormConv2d", "AverageAttention", "VecEmbedding"]
