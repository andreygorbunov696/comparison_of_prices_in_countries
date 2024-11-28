import pandas as pd

class Main():
    def get_data(self):
        return {
                    "Country": ["USA", "Canada", "Germany", "France", "Italy", "Spain", "Japan", "Australia", "Russia", "Belarus",
                                "Ukraine", "Kazakhstan", "Turkey", "Mexico"],
                    "Big Mac Price (USD)": [5.69, 5.56, 4.97, 5.87, 5.87, 5.40, 4.90, 5.07, 1.94, 1.89, 1.90, 2.20, 4.68, 5.19],
                    "Beef Price (USD/kg)": [10.0, 12.0, 9.5, 9.0, 8.5, 8.0, 11.0, 10.5, 6.0, 5.5, 4.0, 4.5, 7.0, 6.5],
                    "Milk Price (USD/L)": [0.99, 1.10, 1.09, 1.05, 1.10, 1.05, 1.12, 1.20, 0.80, 0.75, 0.70, 0.85, 0.95, 0.90],
                    "Egg Price (USD/10)": [3.00, 3.20, 2.50, 2.60, 2.40, 2.30, 3.10, 3.00, 1.50, 1.40, 1.30, 1.20, 2.00, 2.10],
                    "Gasoline Price (USD/L)": [1.20, 1.35, 2.10, 2.05, 2.00, 1.95, 1.45, 1.50, 0.80, 0.75, 0.70, 0.60, 1.30, 1.10],
                    "Rent (USD/month)": [2000, 1800, 1200, 1100, 1000, 900, 900, 1500, 500, 400, 300, 250, 700, 600],
                    "Bread Price (USD/kg)": [3.50, 3.70, 2.50, 2.40, 2.20, 2.10, 2.00, 2.50, 1.20, 1.00, 0.80, 0.70, 1.50, 1.40],
                    "Vodka Price (USD/L)": [15.0, 18.0, 20.0, 22.0, 21.0, 20.0, 25.0, 23.0, 7.0, 6.0, 5.0, 4.5, 12.0, 10.0],
                    "Cabbage Price (USD/kg)": [2.00, 2.10, 1.80, 1.75, 1.70, 1.60, 2.00, 2.10, 1.00, 0.90, 0.80, 0.70, 1.50, 1.30],
                    "Potato Price (USD/kg)": [1.50, 1.60, 1.20, 1.15, 1.10, 1.05, 1.50, 1.40, 0.80, 0.70, 0.60, 0.50, 1.00, 0.90],
                    "Avg Salary (USD/month)": [4000, 3500, 3200, 3000, 2900, 2800, 2800, 3500, 1000, 800, 600, 500, 1200, 1000],
                    "Min Salary (USD/month)": [1500, 1400, 1600, 1500, 1400, 1300, 1100, 1200, 200, 150, 100, 80, 400, 300]
                }
    
    def create_file(self, data):
        df = pd.DataFrame(data)
        output_path = "files/Country_Prices_and_Salaries.xlsx"
        print("File generation has started")
        df.to_excel(output_path, index=False)
        print(f"File saved: {output_path}")

    def __init__(self):
        data = self.get_data()
        self.create_file(data=data)


main = Main()
if __name__ == '__main__':
    main