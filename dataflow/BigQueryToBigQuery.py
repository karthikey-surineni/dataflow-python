import argparse
import logging
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
class BigQueryToBigQuery(beam.DoFn):

    def __init__(self):
        pass
    def process(self, element):
        pass
    def run(argv=None, save_main_session=True):
        '''Main run method'''
        parser = argparse.ArgumentParser()
        parser.add_argument('--input',
                            dest='input',
                            default='cb-dataflow-python:dataflow-output',
                            help='Input table to process')
        parser.add_argument('--output-main',
                            dest='output-main',
                            required=True,
                            help='Output table to write record results to.')
        parser.add_argument('--output-reject',
                            dest='output-reject',
                            required=True,
                            help='Output table to write reject record results to.')
        known_args, pipeline_args = parser.parse_known_args(argv)
        # parser.parse_args(argv)

    if __name__ == '__main__':
        logging.getLogger().setLevel(logging.INFO)
        run()