from so import so_get_jobs
from wework import wework_get_jobs
from remoteok import remoteok_get_jobs


def get_jobs(word):
    jobs = []
    so_jobs = so_get_jobs(word)
    wework_jobs = wework_get_jobs(word)
    remoteok_jobs = remoteok_get_jobs(word)

    len(so_jobs)
    len(wework_jobs)
    len(remoteok_jobs)
    jobs = so_jobs + wework_jobs + remoteok_jobs
    return jobs
