import pandas as pd
import re
import argparse

import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, required=True, help='Path to csv file')
    parser.add_argument('--min_len', type=int, default=99, help='Min length of job requirements')
    parser.add_argument('--save_dir', type=str, required=True)

    args = parser.parse_args()

    df = pd.read_csv(f'{args.data_dir}/fake_job_postings.csv')

    df = df[['title', 'requirements', 'fraudulent']]
    df = df[df['fraudulent'] == 0]

    df.dropna(inplace=True)

    df = df[df['requirements'].str.len() > args.min_len]

    title = df['title'].tolist()
    req = df['requirements'].tolist()

    # Create dir if not exists
    if not os.path.exists(args.save_dir):
        os.mkdir(args.save_dir)

    # Concat Title and Requirements into a line
    with open(f'{args.save_dir}/training.txt', 'w') as f:
        for t, r in zip(title, req):
            data = f"{t} {r}"
            # Split CamelCase word in the string
            data = re.sub(r'([^A-Z])([A-Z])', r'\1 \2', data)
            f.write(f"{data}\n")

    df[['title', 'requirements']].to_csv(f'{args.save_dir}/job_post.csv', index=False)