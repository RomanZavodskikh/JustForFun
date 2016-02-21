#include <algorithm>
#include <cassert>
#include <iostream>

class Node
{
public:
    Node(double* array, unsigned low, unsigned high);
    ~Node();
    double getValue();
    double sum(unsigned from, unsigned to);
    double read(unsigned i);
    double write(unsigned i, double value);
private:
    double value;
    unsigned low, high, mid;
    Node* left;
    Node* right;
};

const double POISON_NUM = 13;
Node* const POISON_PTR = NULL;

Node::Node(double* array, unsigned low, unsigned high)
{
    if (low == high)
    {
        this->value = array[low];
        this->low = this->high = low;
        return;
    }

    if (low > high)
    {
        std::swap(low, high);
    }
    
    this->mid = low/2 + high/2;
    this->low = low;
    this->high = high;
    this->left = new Node(array, low, this->mid);
    this->right = new Node(array, this->mid+1, high);
    this->value = this->left->getValue() + this->right->getValue(); 
}

Node::~Node()
{
    this->value = this->low = this->high = POISON_NUM;
    this->left = this->right = POISON_PTR;
}

double Node::getValue()
{
    return this->value;
}

double Node::sum(unsigned from, unsigned to)
{
    if (from > to)
    {
        std::swap(from, to);
    }
    
    assert (this->low<=from);
    assert (to<=this->high);
    if (from == this->low && to == this->high)
    {
        return this->value;
    }
    else if (from <= this->mid && to <= this->mid)
    {
        return this->left->sum(from, to);
    }
    else if (from <= this->mid && to >= this->mid)
    {
        return this->left->sum(from, this->mid) +
            this->right->sum(this->mid+1, to);
    }
    else if (from >= this->mid && to >= this->mid)
    {
        return this->right->sum(from, to);
    }
    else
    {
        assert(NULL);
    }
}

double Node::write(unsigned i, double value)
{
    assert(this->low<=i<=this->high);    
    double diff = 0.0;
    
    if (this->low==this->high && this->high==i)
    {
        diff = value - this->value;
    }
    else if (i<=this->mid)
    {
        diff = this->left->write(i, value);
    }
    else if (i>this->mid)
    {
        diff = this->right->write(i, value);
    }
    this->value += diff;
    return diff;
}

int main()
{
    double array[8] = {1.0, 21.3, 34.1, 12.5, 12.6, 9.1, 1.0, -9.2};
    Node segtree(array, 0, 7);
    std::cout << segtree.sum(0, 3) << std::endl;
    segtree.write(1, 0.1);
    std::cout << segtree.sum(0, 3) << std::endl;
    return 0;
}
