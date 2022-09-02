# Backend Developer Assignment

https://docs.google.com/document/u/0/d/1S0QMt9MGKhRq8EKEihwwDIxo1bvTcs81ONQ81eiyg9k/mobilebasic


We at Be Zen, are looking for a candidate to help develop, maintain and optimize our backend infrastructure to scale and manage our product as we grow exponentially.


We are a company working in the sustainable consumption space, aimed at the US and European markets. If selected, you would be working with a motley mix of ex-Googlers, INSEAD graduates, doctors and entrepreneurs to develop the product.



## ASSIGNMENT


You need to create a website on which video(s) can be uploaded, processed in some manner (in the background) and then searched using the subtitles in that video as keywords.


For instance, if I were to upload a 2 minute clip of a music video, your application should parse it, apply subtitles to it and ensure that searching for a particular word or phrase returns the time segment within which the video has those phrases being mentioned.


1) You need to use the [**ccextractor**](https://ccextractor.org/) binary for extracting subtitles from video. Note that using any API, etc for subtitle extraction is **not allowed**.


2) Further, after processing, the videos need to be stored in **S3** and the search keywords (subtitles) in **DynamoDB**.


3) HTTP requests should have a maximum latency of approx 1 second.


4) The backend should be preferably written in **Django**. You can use technologies like **Celery** for background tasks.


5) Note that **you will not be judged on the UI** (frontend) of the website you build, hence an extremely simple and functional frontend is acceptable. Judging will be based **solely** on your use of AWS as well as Django.


**"Use this sample video file for running ccextractor”**: https://drive.google.com/file/d/1gLi5ho33TIRNVZkSE-gD4S24zs6Xy1ci/view?usp=sharing


Please host the file.


Please submit in the next 7 days to careers@bezen.eco. If you need more time, please let us know at the same email address. **Host your assignment.**


All the best!
