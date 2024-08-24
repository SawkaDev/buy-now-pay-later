import React, { useEffect, ReactNode } from 'react';
import { useSession } from 'next-auth/react';

interface SessionData {
  sessionData?: string[];
}

function useSessionCookie() {
  const { data: session } = useSession();

  useEffect(() => {
    const typedSession = session as SessionData | null;
    if (typedSession?.sessionData && Array.isArray(typedSession.sessionData)) {
      typedSession.sessionData.forEach((cookie) => {
        document.cookie = cookie.split(';')[0]; // Only set the name=value part
      });
    }
  }, [session]);
}

interface SessionCookieWrapperProps {
  children: ReactNode;
}

const SessionCookieWrapper: React.FC<SessionCookieWrapperProps> = ({ children }) => {
  useSessionCookie();

  return <>{children}</>;
};

export default SessionCookieWrapper;
