package com.example.a7last.model.utils;

import com.example.a7last.exceptions.InterpreterException;

import java.util.List;

public interface MyIList<T> {
    void add(T elem);
    T pop() throws InterpreterException;
    boolean isEmpty();
    List<T> getList();
}
