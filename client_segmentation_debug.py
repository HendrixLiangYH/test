import pandas as pd

class ClientSegmentation:
    def __init__(self, client_data):
        self.client_data = client_data

    def segment_clients(self):
        try:
            # Ensure the client_data is a DataFrame
            if not isinstance(self.client_data, pd.DataFrame):
                raise TypeError("client_data should be a pandas DataFrame")

            # Example segmentation logic based on age and spending
            segments = []
            for index, row in self.client_data.iterrows():
                try:
                    if row['age'] < 30 and row['spending'] < 100:
                        segments.append('Young Low Spender')
                    elif row['age'] < 30 and row['spending'] >= 100:
                        segments.append('Young High Spender')
                    elif row['age'] >= 30 and row['spending'] < 100:
                        segments.append('Adult Low Spender')
                    else:
                        segments.append('Adult High Spender')
                except KeyError as e:
                    print(f'KeyError: {e} - Missing data for index {index}')
                    segments.append('Unknown')
            return segments
        except TypeError as te:
            print(f'TypeError: {te}')
            return None

# Example usage:
# client_data = pd.DataFrame({'age': [25, 35, 45], 'spending': [50, 150, 200]})
# segmenter = ClientSegmentation(client_data)
# print(segmenter.segment_clients())