// contexts/CartContext.tsx
'use client';

import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  useRef,
} from 'react';
import { ProductType } from 'types/products';
import { useSnackbar } from './SnackbarContext';

type CartContextType = {
  items: ProductType[];
  addItem: (item: ProductType) => void;
  removeItem: (id: number) => void;
  clearCart: () => void;
};

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [items, setItems] = useState<ProductType[]>([]);
  const initialized = useRef(false);
  const { showSnackbar } = useSnackbar();

  const handleClick = () => {
    showSnackbar('Added Item to Cart!', 'success');
  };

  useEffect(() => {
    if (!initialized.current) {
      const savedCart = localStorage.getItem('cart');
      if (savedCart) {
        const parsedCart = JSON.parse(savedCart);
        setItems(parsedCart);
      }
      initialized.current = true;
    }
  }, []);

  useEffect(() => {
    if (initialized.current) {
      localStorage.setItem('cart', JSON.stringify(items));
    }
  }, [items]);

  useEffect(() => {
    const handleStorageChange = (event: StorageEvent) => {
      if (event.key === 'cart' && event.newValue) {
        const newCart = JSON.parse(event.newValue);
        setItems(newCart);
      }
    };

    window.addEventListener('storage', handleStorageChange);

    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);

  const addItem = (item: ProductType) => {
    setItems((prevItems) => {
      const existingItem = prevItems.find((i) => i.id === item.id);
      handleClick();
      if (existingItem) {
        return prevItems.map((i) =>
          i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i,
        );
      }
      return [...prevItems, { ...item, quantity: 1 }];
    });
  };

  const removeItem = (id: number) => {
    setItems((prevItems) => prevItems.filter((item) => item.id !== id));
  };

  const clearCart = () => {
    setItems([]);
  };

  return (
    <CartContext.Provider value={{ items, addItem, removeItem, clearCart }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  const context = useContext(CartContext);
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
};
