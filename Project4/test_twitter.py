# # import mathfun as fun
# from pytest import approx

# def test_addints():
# 	assert 1+1 == 2

# # def test_addfloats():
# # 	assert fun.add(1.5, 1.7) == approx(3.1)

import sys
import twitter
sys.path.append('.')

twitter_tweets = twitter.get_all_tweets()

def tweets():
    count = 3
    num = []
    num = twitter.get_all_tweets(twitter_tweets,count)
    assert len(num) == 0
    
    
    
# if __name__ == '__main__':
#     pytest.main("twitter.py")
