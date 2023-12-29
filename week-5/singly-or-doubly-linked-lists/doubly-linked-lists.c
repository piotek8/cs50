
typedef struct dllist
{
    VALUE val;
    struct dllist* prev;
    struct dllist* next;
}
dllnode;


// Insert a new node into the linked list
dllnode* insert(dllnode* head, VALUE val);

// Delete a node from a linked list
void delete(dllnode* target);
