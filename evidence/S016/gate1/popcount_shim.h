/* S016 MSVC build shim only (no S015 source edit): GCC popcount builtins. */
#include <intrin.h>
#define __builtin_popcount(x) ((int)__popcnt((unsigned int)(x)))
#define __builtin_popcountl(x) ((int)__popcnt64((unsigned long long)(x)))
