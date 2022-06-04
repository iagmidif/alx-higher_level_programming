#include "lists.h"
#include <stdio.h>
#define ARR_SIZE 512

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[ARR_SIZE];
	int i, start, end;
	listint_t *h;

	if (head == NULL)
		return (1);
	h = *head;
	i = 0;
	while (h != NULL)
	{
		arr[i] = h->n;
		h = h->next;
		i++;
	}
	start = 0;
	end = i - 1;

	while (start < end)
	{
		if (arr[start] != arr[end])
			return (0);
		start++;
		end--;
	}
	return (1);
}
