#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

def person_a():
    """Reads the data in data/school_performance.csv
    and returns a dataframe with the first 5,000 rows.

    Returns:
    dataframe: containing first 5,000 rows of school_performace.csv
    """
    # Code goes over here.
    return df.head(5000) 
    
    raise NotImplementedError()

https://github.com/freyua911/mlbd-2025.git

def person_c(df):
    """Calculates the mean from the column "grade"

    Parameters:
    df (dataframe): Data from female students

    Returns:
    float: Mean grade
    """
    # Code goes over here.
    mean_female_grade = df[df["gender"].str.lower() == "female"]["grade"].mean()
    return mean_female_grade

    raise NotImplementedError()

def main():
    """ Main program """
    # Code goes over here.
    file_path = "data/school_performance.csv"
    df = pd.read_csv(file_path)
    df = person_a()
    df = person_b(df)
    res = person_c(df)

    print(f"Mean grade of female students is {res}")

if __name__ == "__main__":
    main()