"""Execução da pipeline."""
from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

if __name__ == '__main__':
    data_frame_list = extract_from_excel('../data/input')
    data_frame = concat_data_frames(data_frame_list)
    load_excel(data_frame, '../data/output', 'output')
    print('Pipeline executado com sucesso!')
    print('Arquivo gerado em ../data/output/output.xlsx')
    print('Fim da execução.')
