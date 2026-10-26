// Sceau « SM » de l'étude, dessiné en SVG (couleur héritée via currentColor).
export default function Seal({ ringId, className }) {
  return (
    <svg className={className} viewBox="0 0 240 240" aria-hidden="true" focusable="false">
      <defs>
        <path id={ringId} d="M 120,120 m -86,0 a 86,86 0 1,1 172,0 a 86,86 0 1,1 -172,0" />
      </defs>
      <g fill="none" stroke="currentColor">
        <circle cx="120" cy="120" r="114" strokeWidth="4" />
        <circle cx="120" cy="120" r="106" strokeWidth="1.6" />
        <circle cx="120" cy="120" r="72" strokeWidth="2" />
        <line x1="86" y1="146" x2="154" y2="146" strokeWidth="1.6" />
      </g>
      <g fill="currentColor">
        <text fontFamily="Open Sans, sans-serif" fontSize="14" fontWeight="700">
          <textPath href={`#${ringId}`} textLength="528" lengthAdjust="spacing">
            ÉTUDE DE MAÎTRE SANDRINE MONGOUE • NOTAIRE À DOUALA •
          </textPath>
        </text>
        <text x="120" y="92" textAnchor="middle" fontFamily="Open Sans, sans-serif" fontSize="12" fontWeight="700" letterSpacing="1.5">
          9E CHARGE
        </text>
        <text x="120" y="137" textAnchor="middle" fontFamily="Open Sans, sans-serif" fontSize="44" fontWeight="700">
          SM
        </text>
        <text x="120" y="166" textAnchor="middle" fontFamily="Open Sans, sans-serif" fontSize="12" fontWeight="700" letterSpacing="1.5">
          AKWA
        </text>
      </g>
    </svg>
  );
}

export function BrandMark({ className }) {
  return (
    <svg className={className} viewBox="0 0 40 40" aria-hidden="true">
      <circle cx="20" cy="20" r="18.5" fill="none" stroke="#4B2E83" strokeWidth="1.5" />
      <circle cx="20" cy="20" r="15.4" fill="none" stroke="#4B2E83" strokeWidth="0.75" />
      <text x="20" y="24.6" textAnchor="middle" fontFamily="Open Sans, sans-serif" fontSize="12.5" fontWeight="700" fill="#4B2E83">
        SM
      </text>
    </svg>
  );
}
