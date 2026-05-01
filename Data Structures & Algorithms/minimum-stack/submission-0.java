public class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minstack;

    public MinStack() {
        minstack = new Stack<>();
        stack = new Stack<>();
    }

    public void push(int val) {
        stack.push(val);
        if (minstack.isEmpty() || val <= minstack.peek()) {
            minstack.push(val);
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;
        int top = stack.pop();
        if (!minstack.isEmpty() && top == minstack.peek()) {
            minstack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minstack.peek();
    }
}
