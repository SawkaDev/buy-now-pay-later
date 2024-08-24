// third-party
import { FormattedMessage } from 'react-intl';

// assets
import {
  BorderOutlined,
  BoxPlotOutlined,
  ChromeOutlined,
  DeploymentUnitOutlined,
  GatewayOutlined,
  KeyOutlined,
  LinkOutlined,
  MenuUnfoldOutlined,
  QuestionOutlined,
  SmileOutlined,
  StopOutlined,
} from '@ant-design/icons';

// type
import { NavItemType } from 'types/menu';

// icons
const icons = {
  BorderOutlined,
  BoxPlotOutlined,
  ChromeOutlined,
  DeploymentUnitOutlined,
  GatewayOutlined,
  MenuUnfoldOutlined,
  QuestionOutlined,
  StopOutlined,
  SmileOutlined,
  KeyOutlined,
  LinkOutlined
};

// ==============================|| MENU ITEMS - SUPPORT ||============================== //

const other: NavItemType = {
  id: 'other',
  title: <FormattedMessage id="others" />,
  type: 'group',
  children: [
    {
      id: 'api-keys',
      title: <FormattedMessage id="api-keys" />,
      type: 'item',
      url: '/api-keys',
      icon: icons.KeyOutlined
    },
    {
      id: 'webhooks',
      title: <FormattedMessage id="webhooks" />,
      type: 'item',
      url: '/webhooks',
      icon: icons.LinkOutlined
    },
    {
      id: 'sample-page',
      title: <FormattedMessage id="sample-page" />,
      type: 'item',
      url: '/sample-page',
      icon: icons.ChromeOutlined
    }
  ]
};

export default other;
