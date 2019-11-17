import argparse
import logging
import re
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.metrics import Metrics
from apache_beam.metrics.metric import MetricsFilter
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.internal.clients import bigquery
from BQUtil import BQUtil as bqutil

class RecordToBigQuery(beam.DoFn):

    def __init__(self):
        pass
    def process(self, element):
        pass

        # row = zip()
    def run(argv=None, save_main_session=True):
        '''Main run method'''
        parser = argparse.ArgumentParser()
        parser.add_argument('--input',
                            dest='input',
                            default='gs://cb-dataflow-storage/test-file.csv',
                            help='Input File Path to process')
        parser.add_argument('--output-main',
                            dest='output_main',
                            required=True,
                            help='Output table to write record results to.')
        parser.add_argument('--output-reject',
                            dest='output_reject',
                            required=True,
                            help='Output table to write reject record results to.')
        known_args, pipeline_args = parser.parse_known_args(argv)
        pipeline_options = PipelineOptions(pipeline_args)
        p = beam.Pipeline(options=pipeline_options)

        bqhelper = bqutil()
        output_table_spec = bqhelper.get_table_reference(known_args.output_main)
        output_schema=bqhelper.get_table_schema(known_args.output_main)
        print(output_schema)
        # lines =
        lines = p | 'read' >> ReadFromText(known_args.input,skip_header_lines=1)
        records = lines | 'BigQuery Parse Row' >> beam.Map(lambda s: bqhelper.parse_method(output_schema,s))
        records |'BigQuery Write Row' >> beam.io.WriteToBigQuery(
        output_table_spec,
        schema=output_schema,
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER)

        # | ''
        # output = lines | 'print' >> beam.Map(print)

        # lines | 'bq write' >> beam.io.WriteToBigQuery(
        # output_table_spec,
        # schema=output_schema,
        # write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        # create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER)

        result = p.run()
        # result.wait_until_finish()

    if __name__ == '__main__':
        logging.getLogger().setLevel(logging.INFO)
        run()