#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *is_palindrome - ...
 *head: ...
 *Return: ...
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *front, *rear;
        int i = 0, j, c = 0;
        
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (tmp != NULL)
	{
		tmp = tmp->next;
		c++;
	}
	while (i != c / 2)
	{
		front = rear = *head;
		for (j = 0; j < i; j++)
		{
			front = front->next;
		}
		for (j = 0; j < c - (i + 1); j++)
		{
			rear = rear->next;
		}
		if (front->n != rear->n)
		{
			return (0);
		}
		else
		{
			i++;
		}
	}
	return (1);
}
