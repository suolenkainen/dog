import unittest
import src.neurons as neurons


class Neurons(unittest.TestCase):
    def setUp(self):        

        self.connection = neurons.Connection()
        self.sourceneuron = neurons.sourceneurons()
        self.sinkneuron = neurons.sinkneurons()


    def test_createConnection (self):
                
        # Test connection is created

        self.assertEqual(self.connection.source, 0)
        self.assertEqual(self.connection.sink, 0)
        self.assertEqual(self.connection.weight, 0)


    def test_createNeurons (self):
                
        # Test that neurons are creted

        self.assertEqual(self.sourceneuron, None)
        self.assertEqual(self.sinkneuron, None)
    

if __name__ == '__main__':
    unittest.main()