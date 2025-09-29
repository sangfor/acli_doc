import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
  // 添加链接和背景色属性
  link: string;
  buttonStyle?: React.CSSProperties;
};

const FeatureList: FeatureItem[] = [
  {
    title: '下载安装',
    Svg: require('@site/static/img/download.svg').default,
    description: (
      <>
        下载安装，即可上手。
      </>
    ),
    link: '/docs/next/download', // 根据实际路径修改
    buttonStyle: { backgroundColor: '#3498db' },
  },
  {
    title: '演示教程',
    Svg: require('@site/static/img/tutorial.svg').default,
    description: (
      <>
        观看视频，沉浸体验。
      </>
    ),
    link: '/docs/next/tutorial', // 根据实际路径修改
    buttonStyle: { backgroundColor: '#f39c12' },
  },
  {
    title: '联系我们',
    Svg: require('@site/static/img/contact.svg').default,
    description: (
      <>
        问题需求，欢迎反馈。
      </>
    ),
    link: '/docs/next/contact', // 根据实际路径修改
    buttonStyle: { backgroundColor: '#2ecc71' },
  },
];

function Feature({ title, Svg, description, link, buttonStyle }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        {/* 添加按钮 */}
        <a
          href={link}
          style={{
            ...buttonStyle,
            color: 'white',
            padding: '10px 20px',
            textDecoration: 'none',
            borderRadius: '5px',
            display: 'inline-block',
            marginTop: '10px',
            fontWeight: 'bold',
          }}
        >
          {title}
        </a>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}