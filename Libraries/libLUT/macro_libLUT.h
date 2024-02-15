/*
 * Copyright (C) 2015 ESTEREL TECHNOLOGIES SAS. ALL RIGHTS RESERVED.
 */



#include <math.h>
#include "kcg_types.h"

/* BitwiseNot */
#define BitwiseNot_GPS_LIB_EXTERN(X) ( ~(X) )

/* IsOdd */
#define IsOdd_GPS_LIB_EXTERN(N) ( (N & 1) != 0 )

/* FrExp */
#define FrExp_GPS_LIB_EXTERN(X, F, E) ( *(F) = frexp(X, E) )

/* LdrExp */
#define LdExp_GPS_LIB_EXTERN(F, E) ( ldexp(F, E) )


