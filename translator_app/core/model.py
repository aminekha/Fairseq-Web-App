from fairseq.models.transformer import TransformerModel
import os

def english_to_french(text):
  en_to_fr = TransformerModel.from_pretrained(
    'fairseq_translator/core/pretrained_models/wmt14.en-fr.fconv-py',
    checkpoint_file='model.pt',
    data_name_or_path='fairseq_translator/core/pretrained_models/wmt14.en-fr.fconv-py',
    bpe='fastbpe',
    bpe_codes='fairseq_translator/core/pretrained_models/wmt14.en-fr.fconv-py/bpecodes'
  )
  
  return en_to_fr.translate(text)

# print(en_to_fr.translate('Hello World!'))
