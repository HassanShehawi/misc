#include "stdafx.h"
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

//Givens for the puzzle: 51 fake coins and 50 original ones with difference in weight as 1 gram
const int fake_coins_count = 51;
const int orig_coins_count = 50;
const float coin_weight_diff = 1; //or -1

//solution begins here: assume one of them (the original or the fake) is 5 gram, the other would be 5 (or 4 depending on above line)
float orig_coin_weight = 5;
float fake_coin_weight = 5 + coin_weight_diff;

class coin
{
	float weight;
	std::string type;
public:
	void set_weight(float w) { weight = w; }
	void set_type(std::string t) { type = t; }
	float get_weight() { return weight; }
	std::string get_type() { return type; }
};

std::string check_coin(float weights_diff)
{
	std::string fake_orig = "unknown";
	if (fmod(weights_diff + 51,99) == 0 || fmod((weights_diff - 51), 99) == 0)
		fake_orig = "orig";
	else if (fmod(weights_diff + 49,  99) == 0 || fmod(weights_diff - 49, 99) == 0)
		fake_orig = "fake";
	return fake_orig;
}

int main()
{
	coin coins[orig_coins_count + fake_coins_count];
	coin drawn_coin;
	coin rest_coins[orig_coins_count + fake_coins_count - 1];		


	for (int fake_coin = 0; fake_coin < fake_coins_count; fake_coin++)
	{
		coins[fake_coin].set_weight(fake_coin_weight);
		coins[fake_coin].set_type("fake");
	}
	for (int orig_coin = fake_coins_count; orig_coin < fake_coins_count + orig_coins_count; orig_coin++)
	{
		coins[orig_coin].set_weight(orig_coin_weight);
		coins[orig_coin].set_type("orig");
	}


	srand(time(NULL));
	for (int itr = 0; itr < 100; itr++)
	{		
		int rand_coin_indx = (rand() % 100);
		drawn_coin = coins[rand_coin_indx];

		int mn_indx = 0, cp_inx = 0;
		for (int rc = 0; rc < orig_coins_count + fake_coins_count; rc++)
		{
			if (rc == rand_coin_indx)
				continue;
			else
				rest_coins[cp_inx] = coins[rc];
			cp_inx++;
		}


		coin scale_right[1];
		coin scale_left[100];

		float scale_right_weight = 0, scale_left_weight = 0;

		for (int rr = 0; rr < 100; rr++) scale_left_weight += rest_coins[rr].get_weight();

		float wt_df = scale_left_weight - drawn_coin.get_weight();

		std::cout << scale_left_weight << '\t' << drawn_coin .get_weight() <<'\t' << wt_df << '\t' << wt_df+51 << '\t' << wt_df-51 << '\t' << wt_df+49 << '\t' << wt_df-49 << '\t';
		std::cout << (wt_df + 51) / 99 << '\t' << (wt_df - 51) / 99 << '\t' << (wt_df + 49) / 99 << '\t' << (wt_df - 49) / 99 << '\t' << check_coin(wt_df)<< '\t' << drawn_coin.get_type() << '\n';
	}
	
	int df;
	std::cin >> df;
		

    return 0;
}

