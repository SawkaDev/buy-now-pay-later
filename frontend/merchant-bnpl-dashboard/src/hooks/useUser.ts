// next
import { useQuery } from '@tanstack/react-query';
import { useSession } from 'next-auth/react';
import UserService from 'utils/database-services/Auth';

export interface UserProps {
  name: string;
  email: string;
  avatar: string;
  thumb: string;
  role: string;
  id: number;
}

const useUser = () => {
  const { data: session } = useSession();
  if (session) {
    const user = session?.user;
    const provider = session?.provider;
    let thumb = user?.image!;
    if (provider === 'cognito') {
      const email = user?.email?.split('@');
      user!.name = email ? email[0] : 'Jone Doe';
    }

    if (!user?.image) {
      user!.image = '/assets/images/users/avatar-1.png';
      thumb = '/assets/images/users/avatar-thumb-1.png';
    }

    const { data: userId } = useQuery({
      queryKey: ['userId'],
      queryFn: UserService.checkSession
    });

    const newUser: UserProps = {
      name: user!.name!,
      email: user!.email!,
      avatar: user?.image!,
      thumb,
      role: 'UI/UX Designer',
      id: userId
    };

    return newUser;
  }
  return false;
};

export default useUser;
