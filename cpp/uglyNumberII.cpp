#include <set>
#include <cstdio>

using namespace std;

int nthUglyNumber(int n) {
	set<long long> isUgly;
	isUgly.insert(1);
	long long top = 0;
	for(int i=0; i<n; i++){
		top = *isUgly.lower_bound(top+1);
		printf("%d\n", top);
		isUgly.insert(top*2);
		isUgly.insert(top*3);
		isUgly.insert(top*5);

	}
	return top;
}

int main(int argc, char **argv)
{
	printf("%d\n", nthUglyNumber(10));
}
