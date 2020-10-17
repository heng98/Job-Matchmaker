from JobMatchmaker import JobMatchmaker
from ResumeParser import resume_parser
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True, help='dir path of the data file containing job post')
    parser.add_argument('--resume_path', type=str, required=True, help='path of resume')
    parser.add_argument('--n_jobs', type=int, default=3, help='number of job to output')

    args = parser.parse_args()

    job_matchmaker = JobMatchmaker(args.data_path)
    resume = resume_parser(args.resume_path)

    result = job_matchmaker.get_match_job(resume, args.n_jobs)

    titles = result['title'].tolist()
    reqs = result['requirements'].tolist()

    for t, r in zip(titles, reqs):
        print(t)
        print(r)
        print()