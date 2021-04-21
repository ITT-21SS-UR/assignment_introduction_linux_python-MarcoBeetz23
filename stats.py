{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "129d3b78",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "23cef513",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23.5\n",
      "17.7\n",
      "24.3\n",
      "3.41\n",
      "2.79\n",
      "42.0\n",
      "69.9\n",
      "0.0\n",
      "1.3\n"
     ]
    }
   ],
   "source": [
    "data = open(\"numbers.txt\")\n",
    "nums = data.read()\n",
    "print(nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "84e34eed",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['23.5', '17.7', '24.3', '3.41', '2.79', '42.0', '69.9', '0.0', '1.3']"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_nums = nums.split()\n",
    "\n",
    "my_nums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "440d3d8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(my_nums)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "598fd049",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[23.5, 17.7, 24.3, 3.41, 2.79, 42.0, 69.9, 0.0, 1.3]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i in range(0, len(my_nums)):\n",
    "    my_nums[i] = float(my_nums[i])\n",
    "    \n",
    "    \n",
    "my_nums"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "27a4a3b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>20.544444</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>23.260681</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.790000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>17.700000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>24.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>69.900000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               0\n",
       "count   9.000000\n",
       "mean   20.544444\n",
       "std    23.260681\n",
       "min     0.000000\n",
       "25%     2.790000\n",
       "50%    17.700000\n",
       "75%    24.300000\n",
       "max    69.900000"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(my_nums)\n",
    "\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a77ccdf6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
