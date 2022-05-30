# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sentencepiece
else:
    import _sentencepiece

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SentencePieceProcessor(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _sentencepiece.SentencePieceProcessor_swiginit(self, _sentencepiece.new_SentencePieceProcessor())
    __swig_destroy__ = _sentencepiece.delete_SentencePieceProcessor

    def LoadFromSerializedProto(self, serialized):
        return _sentencepiece.SentencePieceProcessor_LoadFromSerializedProto(self, serialized)

    def SetEncodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetEncodeExtraOptions(self, extra_option)

    def SetDecodeExtraOptions(self, extra_option):
        return _sentencepiece.SentencePieceProcessor_SetDecodeExtraOptions(self, extra_option)

    def SetVocabulary(self, valid_vocab):
        return _sentencepiece.SentencePieceProcessor_SetVocabulary(self, valid_vocab)

    def ResetVocabulary(self):
        return _sentencepiece.SentencePieceProcessor_ResetVocabulary(self)

    def LoadVocabulary(self, filename, threshold):
        return _sentencepiece.SentencePieceProcessor_LoadVocabulary(self, filename, threshold)

    def EncodeAsPieces(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsPieces(self, input)

    def EncodeAsIds(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsIds(self, input)

    def NBestEncodeAsPieces(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsPieces(self, input, nbest_size)

    def NBestEncodeAsIds(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsIds(self, input, nbest_size)

    def SampleEncodeAsPieces(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsPieces(self, input, nbest_size, alpha)

    def SampleEncodeAsIds(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsIds(self, input, nbest_size, alpha)

    def SampleEncodeAndScoreAsPieces(self, input, num_samples, theta, wor, include_best):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAndScoreAsPieces(self, input, num_samples, theta, wor, include_best)

    def SampleEncodeAndScoreAsIds(self, input, num_samples, theta, wor, include_best):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAndScoreAsIds(self, input, num_samples, theta, wor, include_best)

    def DecodePieces(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePieces(self, pieces)

    def CalculateEntropy(self, text, theta):
        return _sentencepiece.SentencePieceProcessor_CalculateEntropy(self, text, theta)

    def EncodeAsSerializedProto(self, input):
        return _sentencepiece.SentencePieceProcessor_EncodeAsSerializedProto(self, input)

    def SampleEncodeAsSerializedProto(self, input, nbest_size, alpha):
        return _sentencepiece.SentencePieceProcessor_SampleEncodeAsSerializedProto(self, input, nbest_size, alpha)

    def NBestEncodeAsSerializedProto(self, input, nbest_size):
        return _sentencepiece.SentencePieceProcessor_NBestEncodeAsSerializedProto(self, input, nbest_size)

    def DecodePiecesAsSerializedProto(self, pieces):
        return _sentencepiece.SentencePieceProcessor_DecodePiecesAsSerializedProto(self, pieces)

    def GetPieceSize(self):
        return _sentencepiece.SentencePieceProcessor_GetPieceSize(self)

    def PieceToId(self, piece):
        return _sentencepiece.SentencePieceProcessor_PieceToId(self, piece)

    def IdToPiece(self, id):
        return _sentencepiece.SentencePieceProcessor_IdToPiece(self, id)

    def GetScore(self, id):
        return _sentencepiece.SentencePieceProcessor_GetScore(self, id)

    def IsUnknown(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnknown(self, id)

    def IsControl(self, id):
        return _sentencepiece.SentencePieceProcessor_IsControl(self, id)

    def IsUnused(self, id):
        return _sentencepiece.SentencePieceProcessor_IsUnused(self, id)

    def IsByte(self, id):
        return _sentencepiece.SentencePieceProcessor_IsByte(self, id)

    def unk_id(self):
        return _sentencepiece.SentencePieceProcessor_unk_id(self)

    def bos_id(self):
        return _sentencepiece.SentencePieceProcessor_bos_id(self)

    def eos_id(self):
        return _sentencepiece.SentencePieceProcessor_eos_id(self)

    def pad_id(self):
        return _sentencepiece.SentencePieceProcessor_pad_id(self)

    def serialized_model_proto(self):
        return _sentencepiece.SentencePieceProcessor_serialized_model_proto(self)

    def LoadFromFile(self, arg):
        return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)

    def DecodeIdsWithCheck(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIdsWithCheck(self, ids)

    def DecodeIdsAsSerializedProtoWithCheck(self, ids):
        return _sentencepiece.SentencePieceProcessor_DecodeIdsAsSerializedProtoWithCheck(self, ids)

    def _EncodeAsIds(self, text, enabele_sampling, nbest_size, alpha, add_bos, add_eos, reverse):
        return _sentencepiece.SentencePieceProcessor__EncodeAsIds(self, text, enabele_sampling, nbest_size, alpha, add_bos, add_eos, reverse)

    def _EncodeAsPieces(self, text, enabele_sampling, nbest_size, alpha, add_bos, add_eos, reverse, emit_unk_piece):
        return _sentencepiece.SentencePieceProcessor__EncodeAsPieces(self, text, enabele_sampling, nbest_size, alpha, add_bos, add_eos, reverse, emit_unk_piece)

    def _NBestEncodeAsIds(self, text, nbest_size, add_bos, add_eos, reverse):
        return _sentencepiece.SentencePieceProcessor__NBestEncodeAsIds(self, text, nbest_size, add_bos, add_eos, reverse)

    def _NBestEncodeAsPieces(self, text, nbest_size, add_bos, add_eos, reverse, emit_unk_piece):
        return _sentencepiece.SentencePieceProcessor__NBestEncodeAsPieces(self, text, nbest_size, add_bos, add_eos, reverse, emit_unk_piece)

    def _SampleEncodeAndScoreAsIds(self, text, num_samples, theta, wor, include_best, add_bos, add_eos, reverse):
        return _sentencepiece.SentencePieceProcessor__SampleEncodeAndScoreAsIds(self, text, num_samples, theta, wor, include_best, add_bos, add_eos, reverse)

    def _SampleEncodeAndScoreAsPieces(self, text, num_samples, theta, wor, include_best, add_bos, add_eos, reverse, emit_unk_piece):
        return _sentencepiece.SentencePieceProcessor__SampleEncodeAndScoreAsPieces(self, text, num_samples, theta, wor, include_best, add_bos, add_eos, reverse, emit_unk_piece)

    def Init(self,
             model_file=None,
             model_proto=None,
             out_type=int,
             add_bos=False,
             add_eos=False,
             reverse=False,
             emit_unk_piece=False,
             enable_sampling=False,
             nbest_size=-1,
             alpha=0.1):
      """Initialzie sentencepieceProcessor.

      Args:
        model_file: The sentencepiece model file path.
        model_proto: The sentencepiece model serialized proto.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after
          reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        emit_unk_piece: Emits the unk literal string (Default = false)
        nbest_size: sampling parameters for unigram. Invalid for BPE-Dropout.
                    nbest_size = {0,1}: No sampling is performed.
                    nbest_size > 1: samples from the nbest_size results.
                    nbest_size < 0: assuming that nbest_size is infinite and samples
                      from the all hypothesis (lattice) using
                      forward-filtering-and-backward-sampling algorithm.
        alpha: Soothing parameter for unigram sampling, and dropout probability of
          merge operations for BPE-dropout.
      """

      _sentencepiece_processor_init_native(self)
      self._out_type = out_type
      self._add_bos = add_bos
      self._add_eos = add_eos
      self._reverse = reverse
      self._emit_unk_piece = emit_unk_piece
      self._enable_sampling = enable_sampling
      self._nbest_size = nbest_size
      self._alpha = alpha
      if model_file or model_proto:
        self.Load(model_file=model_file, model_proto=model_proto)


    def Encode(self,
               input,
               out_type=None,
               add_bos=None,
               add_eos=None,
               reverse=None,
               emit_unk_piece=None,
               enable_sampling=None,
               nbest_size=None,
               alpha=None):
      """Encode text input to segmented ids or tokens.

        Args:
        input: input string. accepsts list of string.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after
          reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        emit_unk_piece: Emits the unk literal string (Default = false)
        nbest_size: sampling parameters for unigram. Invalid for BPE-Dropout.
                    nbest_size = {0,1}: No sampling is performed.
                    nbest_size > 1: samples from the nbest_size results.
                    nbest_size < 0: assuming that nbest_size is infinite and samples
                      from the all hypothesis (lattice) using
                      forward-filtering-and-backward-sampling algorithm.
        alpha: Soothing parameter for unigram sampling, and merge probability for
               BPE-dropout (probablity 'p' in BPE-dropout paper).
      """

      if out_type is None:
        out_type = self._out_type
      if add_bos is None:
        add_bos = self._add_bos
      if add_eos is None:
        add_eos = self._add_eos
      if reverse is None:
        reverse = self._reverse
      if emit_unk_piece is None:
        emit_unk_piece = self._emit_unk_piece
      if enable_sampling is None:
        enable_sampling = self._enable_sampling
      if nbest_size is None:
        nbest_size = self._nbest_size
      if alpha is None:
        alpha = self._alpha

      if enable_sampling == True and (nbest_size is None or nbest_size == 0 or
                                      nbest_size == 1 or alpha is None):
        raise RuntimeError(
            'When enable_sampling is True, We must specify "nbest_size > 1" or "nbest_size = -1", '
            'and "alpha". "nbest_size" is enabled only on unigram mode ignored in BPE-dropout. '
            'when "nbest_size = -1" , this method samples from all candidates on the lattice '
            'instead of nbest segmentations.'
        )

      def _encode(text):
        if out_type is int:
          return self._EncodeAsIds(text, enable_sampling, nbest_size,
                                   alpha, add_bos, add_eos, reverse)
        else:
          return self._EncodeAsPieces(text, enable_sampling, nbest_size,
                                      alpha, add_bos, add_eos, reverse, emit_unk_piece)

      if type(input) is list:
        return [_encode(n) for n in input]

      return _encode(input)


    def NBestEncode(self,
                    input,
                    out_type=None,
                    add_bos=None,
                    add_eos=None,
                    reverse=None,
                    emit_unk_piece=None,
                    nbest_size=None):
      """NBestEncode text input to segmented ids or tokens.

        Args:
        input: input string. accepsts list of string.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        emit_unk_piece: Emits the unk literal string (Default = false)
        nbest_size: nbest size
      """

      if out_type is None:
        out_type = self._out_type
      if add_bos is None:
        add_bos = self._add_bos
      if add_eos is None:
        add_eos = self._add_eos
      if reverse is None:
        reverse = self._reverse
      if emit_unk_piece is None:
        emit_unk_piece = self._emit_unk_piece
      if nbest_size is None:
        nbest_size = self._nbest_size

      if nbest_size <= 0:
        nbest_size=1

      def _encode(text):
        if out_type is int:
          return self._NBestEncodeAsIds(text, nbest_size, add_bos, add_eos, reverse)
        else:
          return self._NBestEncodeAsPieces(text, nbest_size, add_bos, add_eos, reverse, emit_unk_piece)

      if type(input) is list:
        return [_encode(n) for n in input]

      return _encode(input)


    def SampleEncodeAndScore(self,
                             input,
                             out_type=None,
                             add_bos=None,
                             add_eos=None,
                             reverse=None,
                             emit_unk_piece=None,
                             num_samples=None,
                             theta=None,
                             wor=None,
                             include_best=None):
      """SampleEncodeAndScore text input to segmented ids or tokens.

        Args:
        input: input string. accepsts list of string.
        out_type: output type. int or str.
        add_bos: Add <s> to the result (Default = false)
        add_eos: Add </s> to the result (Default = false) <s>/</s> is added after reversing (if enabled).
        reverse: Reverses the tokenized sequence (Default = false)
        emit_unk_piece: Emits the unk literal string (Default = false)
        num_samples: How many samples to return (Default = 1)
        theta: inverse temperature for sampling
        wor: whether to sample without replacement (Default = false)
        include_best: whether to include the best tokenization, requires wor=True (Default = false)
      """

      if out_type is None:
        out_type = self._out_type
      if add_bos is None:
        add_bos = self._add_bos
      if add_eos is None:
        add_eos = self._add_eos
      if reverse is None:
        reverse = self._reverse
      if emit_unk_piece is None:
        emit_unk_piece = self._emit_unk_piece
      if num_samples is None:
        num_samples = 1
      if theta is None:
        theta = 1.
      if wor is None:
        wor = False
      if include_best is None:
        include_best = False

      if num_samples <= 0:
        raise RuntimeError('num_examples must be positive')

      if include_best and not wor:
        raise RuntimeError('When include_best is True, We must specify "wor = True".')


      def _encode(text):
        if out_type is int:
          return self._SampleEncodeAndScoreAsIds(text, num_samples, theta, wor, include_best,
                                                 add_bos, add_eos, reverse)
        else:
          return self._SampleEncodeAndScoreAsPieces(text, num_samples, theta, wor, include_best,
                                                    add_bos, add_eos, reverse, emit_unk_piece)

      if type(input) is list:
        return [_encode(n) for n in input]

      return _encode(input)


    def Decode(self, input):
      """Decode processed id or token sequences."""

      if not input:
        return self.DecodeIds([])
      elif type(input) is int:
        return self.DecodeIdsWithCheck([input])
      elif type(input) is str:
        return self.DecodePieces([input])

      def _decode(input):
        if not input:
          return self.DecodeIds([])
        if type(input[0]) is int:
          return self.DecodeIdsWithCheck(input)
        return self.DecodePieces(input)

      if type(input[0]) is list:
        return [_decode(n) for n in input]

      return _decode(input)


    def Entropy(self, input, theta):
      """Calculate sentence entropy"""

      if type(input) is list:
        return [self.CalculateEntropy(n, theta) for n in input]
      return self.CalculateEntropy(input, theta)


    def piece_size(self):
      return self.GetPieceSize()


    def vocab_size(self):
      return self.GetPieceSize()


    def __getstate__(self):
      return self.serialized_model_proto()


    def __setstate__(self, serialized_model_proto):
      self.__init__()
      self.LoadFromSerializedProto(serialized_model_proto)


    def __len__(self):
      return self.GetPieceSize()


    def __getitem__(self, piece):
      return self.PieceToId(piece)


    def Load(self, model_file=None, model_proto=None):
      """Overwride SentencePieceProcessor.Load to support both model_file and model_proto.

      Args:
        model_file: The sentencepiece model file path.
        model_proto: The sentencepiece model serialized proto. Either `model_file`
          or `model_proto` must be set.
      """
      if model_file and model_proto:
        raise RuntimeError('model_file and model_proto must be exclusive.')
      if model_proto:
        return self.LoadFromSerializedProto(model_proto)
      return self.LoadFromFile(model_file)


# Register SentencePieceProcessor in _sentencepiece:
_sentencepiece.SentencePieceProcessor_swigregister(SentencePieceProcessor)


def SetRandomGeneratorSeed(seed):
    return _sentencepiece.SetRandomGeneratorSeed(seed)
class SentencePieceTrainer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    @staticmethod
    def _TrainFromString(arg):
        return _sentencepiece.SentencePieceTrainer__TrainFromString(arg)

    @staticmethod
    def _TrainFromMap(args):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap(args)

    @staticmethod
    def _TrainFromMap2(args, iter):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap2(args, iter)

    @staticmethod
    def _TrainFromMap3(args):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap3(args)

    @staticmethod
    def _TrainFromMap4(args, iter):
        return _sentencepiece.SentencePieceTrainer__TrainFromMap4(args, iter)

    @staticmethod
    def _Train(arg=None, **kwargs):
      """Train Sentencepiece model. Accept both kwargs and legacy string arg."""
      if arg is not None and type(arg) is str:
        return SentencePieceTrainer._TrainFromString(arg)

      def _encode(value):
        """Encode value to CSV.."""
        if type(value) is list:
          if sys.version_info[0] == 3:
            f = StringIO()
          else:
            f = BytesIO()
          writer = csv.writer(f, lineterminator='')
          writer.writerow([str(v) for v in value])
          return f.getvalue()
        else:
          return str(value)

      sentence_iterator = None
      model_writer = None
      new_kwargs = {}
      for key, value in kwargs.items():
        if key in ['sentence_iterator', 'sentence_reader']:
          sentence_iterator = value
        elif key in ['model_writer']:
          model_writer = value
        else:
          new_kwargs[key] = _encode(value)

      if model_writer:
        if sentence_iterator:
          model_proto = SentencePieceTrainer._TrainFromMap4(new_kwargs,
                                                           sentence_iterator)
        else:
          model_proto = SentencePieceTrainer._TrainFromMap3(new_kwargs)
        model_writer.write(model_proto)
      else:
        if sentence_iterator:
          return SentencePieceTrainer._TrainFromMap2(new_kwargs, sentence_iterator)
        else:
          return SentencePieceTrainer._TrainFromMap(new_kwargs)

      return None

    @staticmethod
    def Train(arg=None, logstream=None, **kwargs):
      with _LogStream(ostream=logstream):
        SentencePieceTrainer._Train(arg=arg, **kwargs)


# Register SentencePieceTrainer in _sentencepiece:
_sentencepiece.SentencePieceTrainer_swigregister(SentencePieceTrainer)

def SentencePieceTrainer__TrainFromString(arg):
    return _sentencepiece.SentencePieceTrainer__TrainFromString(arg)

def SentencePieceTrainer__TrainFromMap(args):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap(args)

def SentencePieceTrainer__TrainFromMap2(args, iter):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap2(args, iter)

def SentencePieceTrainer__TrainFromMap3(args):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap3(args)

def SentencePieceTrainer__TrainFromMap4(args, iter):
    return _sentencepiece.SentencePieceTrainer__TrainFromMap4(args, iter)



import re
import csv
import sys
import os
from io import StringIO
from io import BytesIO


def _add_snake_case(classname):
  """Added snake_cased method from CammelCased method."""

  snake_map = {}
  for k, v in classname.__dict__.items():
    if re.match(r'^[A-Z]+', k):
      snake = re.sub(r'(?<!^)(?=[A-Z])', '_',
                     k).lower().replace('n_best', 'nbest')
      snake_map[snake] = v
  for k, v in snake_map.items():
    setattr(classname, k, v)


def _batchnize(classname, name):
  """Enables batch request for the method classname.name."""
  func = getattr(classname, name, None)
  def _func(v, n):
    if type(n) is int and (n < 0 or n >= v.piece_size()):
      raise IndexError('piece id is out of range.')
    return func(v, n)

  def _batched_func(self, arg):
    if type(arg) is list:
      return [_func(self, n) for n in arg]
    else:
      return _func(self, arg)

  setattr(classname, name, _batched_func)


_sentencepiece_processor_init_native = SentencePieceProcessor.__init__
setattr(SentencePieceProcessor, '__init__', SentencePieceProcessor.Init)

SentencePieceProcessor.Tokenize = SentencePieceProcessor.Encode
SentencePieceProcessor.Detokenize = SentencePieceProcessor.Decode
SentencePieceProcessor.DecodeIds = SentencePieceProcessor.DecodeIdsWithCheck
SentencePieceProcessor.DecodeIdsAsSerializedProto = SentencePieceProcessor.DecodeIdsAsSerializedProtoWithCheck

for m in [
    'PieceToId', 'IdToPiece', 'GetScore', 'IsUnknown', 'IsControl', 'IsUnused',
    'IsByte'
]:
  _batchnize(SentencePieceProcessor, m)

_add_snake_case(SentencePieceProcessor)
_add_snake_case(SentencePieceTrainer)
set_random_generator_seed = SetRandomGeneratorSeed

from ._version import __version__

class _LogStream(object):
  def __init__(self, ostream=None):
    self.ostream = ostream
    if self.ostream is not None:
      self.orig_stream_fileno = sys.stderr.fileno()

  def __enter__(self):
    if self.ostream is not None:
      self.orig_stream_dup = os.dup(self.orig_stream_fileno)
      os.dup2(self.ostream.fileno(), self.orig_stream_fileno)

  def __exit__(self, type, value, traceback):
    if self.ostream is not None:
      os.close(self.orig_stream_fileno)
      os.dup2(self.orig_stream_dup, self.orig_stream_fileno)
      os.close(self.orig_stream_dup)
      self.ostream.close()



