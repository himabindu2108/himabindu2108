{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c9228d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "string = input(\"Read an input string: \")\n",
    "for i in range(2):\n",
    "    string = string.replace(string[-2], \"\")\n",
    "print(string[::-1])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
