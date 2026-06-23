def bert_match(resume_text, job_description):

    resume_words = set(
        resume_text.lower().split()
    )

    jd_words = set(
        job_description.lower().split()
    )

    if len(jd_words) == 0:
        return 0

    common = resume_words.intersection(jd_words)

    score = (
        len(common) /
        len(jd_words)
    ) * 100

    return round(score, 2)
