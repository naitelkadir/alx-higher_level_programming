#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
/**
 * reverse_list - ...
 * @head: ...
 * Return: ...
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;
	
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - ...
 * @head: ...
 * Return: ...
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *tmp = *head, *node = NULL;
	
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			node = slow->next;
			break;
		}
		if (!fast-<next)
		{
			node = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&node);
	while (node && tmp)
	{
		if (tmp->n == node->n)
		{
			node = node->next;
			tmp = tmp->next;
		}
		else
		{
			return (0);
		}
	}
	if (!node)
	{
		return (1);
	}
	return (0);
}
