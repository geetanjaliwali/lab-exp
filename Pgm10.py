import csv
class DataSummaryGenerator:

    def __init__ (self, filename):
        self.filename = filename
        self.data = self.read_csv_to_dict()
       

    def read_csv_to_dict(self):
        """
        Reads CSV and converts it into dictionary form:
        {column_name: [values]} """

        data_dict = {}
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key, value in row.items():
                    if key not in data_dict:
                        data_dict[key] = []
                    try:
                        data_dict[key].append(float(value))
                    except ValueError:
                        data_dict[key].append(value)
        print("dictionary",data_dict)
        return data_dict

    def max_value(self, column):
        return max(self.data[column])

    def min_value(self, column):
        return min(self.data[column])

    def average_value(self, column):
        values = self.data[column]
        numeric_values = [v for v in values if isinstance(v, (int, float))]
        return sum(numeric_values) / len(numeric_values)

filename = input("Enter CSV file name: ")
obj = DataSummaryGenerator(filename)

column = input("Enter column name (e.g., Temp, death etc): ")

max_val = obj.max_value(column)
min_val = obj.min_value(column)
avg_val = obj.average_value(column)

with open("summary.txt", "w") as f:
    f.write("DATA SUMMARY GENERATOR REPORT\n")
    f.write("=============================\n\n")
    
    f.write(f"Input File : {filename}\n")
    f.write(f"Column     : {column}\n\n")
    
    f.write("--------------------------------\n")
    f.write("SUMMARY RESULTS\n")
    f.write("--------------------------------\n")
    
    f.write(f"Maximum Value : {max_val}\n")
    f.write(f"Minimum Value : {min_val}\n")
    f.write(f"Average Value : {avg_val}\n\n")
    
    f.write("--------------------------------\n")
    f.write("END OF REPORT\n")
    f.write("--------------------------------\n")
