# HPV_Twitter_Corpus
We provide the annotations for the HPV vaccine Twitter corpus that was used in "Use of deep learning to analyze Social Media discussions about the Human Papillomavirus Vaccine", as well as a Python script to download the tweets.

## NOTE

Please note that by downloading the Twitter data you agree to follow the Twitter terms of service (https://twitter.com/tos?lang=en), which requires not to redistribute the data and to delete tweets that are marked deleted in the future.
You MUST NOT re-distribute the tweets, as this violates the Twitter Terms of Use.

## DATA
The annotations for Tweets corpus are saved in "hpv_twitter_annotation.tsv".

The file contain tab separated information about Tweet IDs and their annotations for each theoretical constructs of behavior change theories.

## DOWNLOAD

Before you download the Twitter data, please first register as a Twitter developer and get Twitter API keys and tokens: https://developer.twitter.com/en/docs/basics/authentication/overview 

In "downloadTweet.py", please specify the keys and tokens from Twitter API and change addresses for both input and output files.

Note that some tweets are not public available currently. In the output file, we leave the text blank if it is not available public.

## CONTACT

Jingcheng Du, jingcheng.du@uth.tmc.edu
Cui Tao, cui.tao@uth.tmc.edu

## RESEARCH GROUP INFORMATION

Center for Biomedical Semantics and Data Intelligence
School of Biomedical Informatics
University of Texas Health Science Center at Houston
https://sbmi.uth.edu/bsdi/

UPDATE DATE:
10/20/2020
