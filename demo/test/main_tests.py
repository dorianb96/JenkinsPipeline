import unittest
try:
    from demo.src import data_wrangler
except ImportError:
    from .demo.src import data_wrangler


class TestStringMethods(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestStringMethods, self).__init__(*args, **kwargs)
        self.filename = 'data/demo.csv'

    def test_read(self):
        df = data_wrangler.read_pandas_dataframe(self.filename)
        self.assertEqual(len(df), 3)
        self.assertListEqual(df.columns.tolist(), ['id','name','date_registration'])

    def test_filter(self):
        df = data_wrangler.read_pandas_dataframe(self.filename)
        df_filtered = tc.filter_bad_names(df)
        self.assertEqual(len(df_filtered),2)


if __name__ == '__main__':
    unittest.main()
